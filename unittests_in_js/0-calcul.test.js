const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber(1, 3), 4);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber(1, 3.7), 5);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber(1.2, 3.7), 5);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber(1.5, 3.7), 6);
    });
});
