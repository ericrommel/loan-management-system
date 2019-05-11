import uuid

from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(verbose_name=_("date"))
    updated = models.DateTimeField(verbose_name=_("updated"), auto_now_add=True)
    active = models.BooleanField(verbose_name=_("active"), default=True)

    class Meta:
        abstract = True


class Loan(Base):
    amount = models.FloatField(verbose_name=_("amount"))
    term = models.IntegerField(verbose_name=_("term"))
    rate = models.FloatField(verbose_name=_("rate"))

    def balance(self, date: timezone.datetime = timezone.now()) -> dict:
        debit = self.installment * self.term
        credit = sum(
            self.payment_set.filter(payment=Payment.MADE, date__lte=date).values_list("amount", flat=True)
        )
        return {"balance": debit - credit}

    @property
    def installment(self) -> float:
        r = self.rate / self.term
        return (r + r / ((1 + r) ** self.term - 1)) * self.amount

    def __str__(self) -> str:
        return f"{self.id}"


class Payment(Base):

    MADE = "made"
    MISSED = "missed"
    PAYMENTS = ((MADE, "made"), (MISSED, "missed"))
    loan = models.ForeignKey(
        to="api.Loan", verbose_name=_("loan"), on_delete=models.CASCADE
    )

    payment = models.CharField(
        verbose_name=_("payment"), max_length=6, choices=PAYMENTS, default=MISSED
    )
    amount = models.FloatField(verbose_name=_("amount"))

    def __str__(self) -> str:
        return str(self.id)
