const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
    let calculateNumberStub;
    let consoleLogSpy;

    beforeEach(function() {
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        calculateNumberStub.restore();
        consoleLogSpy.restore();
    });

    it('should call Utils.calculateNumber with the correct arguments', function() {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnceWithExactly(calculateNumberStub, 'SUM', 100, 20);
    });

    it('should log the correct message', function() {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnceWithExactly(consoleLogSpy, 'The total is: 10');
    });
});
