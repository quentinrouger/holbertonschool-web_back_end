const request = require('supertest');
const server = require('./api');

describe('Index page', () => {
  it('should return status code 200', async () => {
    const response = await request(server).get('/');
    expect(response.statusCode).toEqual(200);
  });

  it('should return the correct result', async () => {
    const response = await request(server).get('/');
    expect(response.text).toEqual('Welcome to the payment system');
  });
});
