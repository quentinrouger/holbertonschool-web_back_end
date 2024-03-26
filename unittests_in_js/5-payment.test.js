const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
    let consoleLogSpy;

    beforeEach(function() {
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        consoleLogSpy.restore();
    });

    it('should log the correct message for total amount of 100 and total shipping of 20', function() {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnceWithExactly(consoleLogSpy, 'The total is: 120');
    });

    it('should log the correct message for total amount of 10 and total shipping of 10', function() {
        sendPaymentRequestToApi(10, 10);
        sinon.assert.calledOnceWithExactly(consoleLogSpy, 'The total is: 20');
    });
});
