// Function to fetch fingerprint data
function fetchFingerprintData() {
  fetch('fingerprint_data.json')
    .then(response => response.json())
    .then(data => {
      const tableBody = document.getElementById('attendanceTableBody');
      tableBody.innerHTML = ''; // Clear the existing table body

      // Loop through the fingerprint data and create table rows
      data.forEach(fingerprint => {
        const row = document.createElement('tr');

        // Create table cells for ID and Timestamp
        const idCell = document.createElement('td');
        idCell.textContent = fingerprint.id;
        row.appendChild(idCell);

        const timestampCell = document.createElement('td');
        timestampCell.textContent = fingerprint.timestamp;
        row.appendChild(timestampCell);

        // Append the row to the table body
        tableBody.appendChild(row);
      });
    })
    .catch(error => {
      console.log('Error fetching fingerprint data:', error);
    });
}

// Call the fetchFingerprintData function on page load
window.addEventListener('DOMContentLoaded', fetchFingerprintData);

