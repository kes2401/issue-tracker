$(function () {
    $('#payment-form').submit(function () {
        const form = this;
        const card = {
            number: $('#id_credit_card_no').val(),
            exp_month: $('#id_expiry_month').val(),
            exp_year: $('#id_expiry_year').val(),
            cvc: $('#id_cvv').val()
        }

        Stripe.card.createToken(card, function (status, response) {

            if (status === 200) {

                $('#credit-card-errors').hide();
                $('#id_stripe_id').val(response.id);

                // Prevent the Credit Card Details from being submitted to our server
                $('#id_credit_card_number').removeAttr('name');
                $('#id_cvv').removeAttr('name');
                $('#id_expiry_month').removeAttr('name');
                $('#id_expiry_year').removeAttr('name');

                form.submit();

            } else {
                $('#stripe-error-message').text(response.error.message);
                $('#credit-card-errors').show();
                $('#validate_card_btn').attr('disabled', false);
            }
        });

        return false;
    });

})