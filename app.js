<script>
  function handleSubmit(event) {
    event.preventDefault();

    const data = {
      requestedFor: document.getElementById('requestedFor').value,
      requestType: document.querySelector('input[name="requestType"]:checked')?.value,
      accountType: document.querySelector('input[name="accountType"]:checked')?.value,
      accessLevel: document.querySelector('input[name="accessLevel"]:checked')?.value,
      serverNames: document.getElementById('serverNames').value,
      userList: document.getElementById('userList').value,
      employeeId: document.getElementById('employeeId').value,
      centrifyList: document.getElementById('centrifyList').value,
      boksList: document.getElementById('boksList').value,
      profileList: document.getElementById('profileList').value
    };

    fetch('http://localhost:5000/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
      if (res.ticketNumber) {
        window.location.href = '/tickets'; // 🚀 Redirect here
      } else {
        alert("Failed to submit ticket");
      }
    })
    .catch(err => alert("Error: " + err));
  }
</script>
