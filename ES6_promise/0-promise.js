function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an API call, e.g., fetching data from an API
    setTimeout(() => {
      // For this example, we'll resolve the Promise with a sample response
      const sampleResponse = { message: "Hello, this is your API response!" };
      resolve(sampleResponse);
    }, 2000); // Simulating a 2-second delay (adjust as needed)
  });
}

export default getResponseFromAPI;
