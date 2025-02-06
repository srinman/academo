import requests
import time
import matplotlib.pyplot as plt
from flask import Flask, send_file
import threading

# Configuration
ENDPOINT = "https://aca1bookstoreflaky.yellowwater-6d602683.westus2.azurecontainerapps.io/unstable-endpoint"
# ENDPOINT = "https://acabookstoreflaky2.salmonglacier-101b4341.westus2.azurecontainerapps.io/unstable-endpoint"

NUM_REQUESTS = 100

# Statistics
failures = 0
successes = 0
response_times = []

# Record the start time of the test
test_start_time = time.time()

# Simulate HTTP calls
for _ in range(NUM_REQUESTS):
    start_time = time.time()
    try:
        response = requests.get(ENDPOINT)
        response_time = time.time() - start_time
        response_times.append(response_time)
        if response.status_code == 200:
            successes += 1
        else:
            failures += 1
    except requests.RequestException:
        failures += 1
        response_times.append(float('inf'))

# Record the end time of the test
test_end_time = time.time()
total_test_time = test_end_time - test_start_time

# Calculate statistics
average_response_time = sum(response_times) / len(response_times)
max_response_time = max(response_times)
min_response_time = min(response_times)

# Print statistics
print(f"Number of failures: {failures}")
print(f"Number of successes: {successes}")
print(f"Average response time: {average_response_time:.2f} seconds")
print(f"Max response time: {max_response_time:.2f} seconds")
print(f"Min response time: {min_response_time:.2f} seconds")
print(f"Total test time: {total_test_time:.2f} seconds")

# Generate response time chart
plt.figure(figsize=(10, 5))
plt.plot(response_times, label='Response Time')
plt.axhline(y=average_response_time, color='r', linestyle='-', label='Average Response Time')
plt.xlabel('Request Number')
plt.ylabel('Response Time (seconds)')
plt.title('Response Time Analysis with Resiliency')
plt.legend()
plt.savefig('response_times_chart.jpg')

# Generate success vs failure chart
labels = ['Successes', 'Failures']
sizes = [successes, failures]
colors = ['#4CAF50', '#FF6347']
explode = (0.1, 0)  # explode the 1st slice (Successes)

plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Success vs Failure Rate')
plt.savefig('success_failure_chart.jpg')

# Serve charts using Flask
app = Flask(__name__)

@app.route('/')
def serve_charts():
    return '''
    <h1>Resiliency Test Results</h1>
    <h2>Response Time Analysis</h2>
    <img src="/response_times_chart.jpg" alt="Response Time Chart">
    <h2>Success vs Failure Rate</h2>
    <img src="/success_failure_chart.jpg" alt="Success vs Failure Chart">
    <h2>Total Test Time</h2>
    <p>Total test time: {:.2f} seconds</p>
    '''.format(total_test_time)

@app.route('/response_times_chart.jpg')
def serve_response_times_chart():
    return send_file('response_times_chart.jpg', mimetype='image/jpeg')

@app.route('/success_failure_chart.jpg')
def serve_success_failure_chart():
    return send_file('success_failure_chart.jpg', mimetype='image/jpeg')

def run_flask():
    app.run(host='0.0.0.0', port=5001)

# Run Flask server in a separate thread
thread = threading.Thread(target=run_flask)
thread.start()
