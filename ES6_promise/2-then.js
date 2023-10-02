function handleResponseFromAPI(promise) {
  if (promise) {
    return Promise.resolve({
      status: 200,
      body: 'Success',
    }).then(() => console.log('Got a response from the API'));
  }
  return Promise.reject(new Error(''));
}

export default handleResponseFromAPI;
