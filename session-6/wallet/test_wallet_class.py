from wallet import Wallet, InsufficientAmount
import pytest


class TestWallet:
    def test_default_initial_balance(self):
        wallet = Wallet()
        assert wallet.balance == 0

    def test_setting_initial_amount(self):
        wallet = Wallet(100)

        assert wallet.balance == 100

    @pytest.mark.skip("Sample reason for skipping the test.")
    @pytest.mark.smoke
    def test_wallet_add_cash(self):
        wallet = Wallet(10)
        wallet.add_cash(90)

        assert wallet.balance == 100

    @pytest.mark.smoke
    def test_wallet_spend_cash(self):
        wallet = Wallet(20)
        wallet.spend_cash(10)

        assert wallet.balance == 10

    @pytest.mark.smoke
    def test_wallet_spend_cash_raises_exception_on_insufficient_amount(self):
        wallet = Wallet()

        with pytest.raises(InsufficientAmount):
            wallet.spend_cash(100)

    @pytest.mark.parametrize(
        "earned, spent, expected_balance", [(100, 50, 50), (50, 20, 30), (60, 30, 30),]
    )
    def test_transactions(self, earned, spent, expected_balance):
        wallet = Wallet()
        wallet.add_cash(earned)
        wallet.spend_cash(spent)

        assert wallet.balance == expected_balance
