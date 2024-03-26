const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
    let calculateNumberSpy;

    beforeEach(function() {
        calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    });

    afterEach(function() {
        calculateNumberSpy.restore();
    });

    it('should call Utils.calculateNumber with the correct arguments', function() {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnce(calculateNumberSpy);
        sinon.assert.calledWithExactly(calculateNumberSpy, 'SUM', 100, 20);
    });
});
