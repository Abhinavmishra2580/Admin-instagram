<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        table { width: 80%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; }
    </style>
</head>
<body>

    <h2>Admin Panel</h2>
    <table id="userTable">
        <tr>
            <th>User ID</th>
            <th>Password</th>
        </tr>
    </table>

    <script>
        function fetchData() {
            fetch('/admin-data')
            .then(response => response.json())
            .then(users => {
                let table = document.getElementById("userTable");
                table.innerHTML = "<tr><th>User ID</th><th>Password</th></tr>";
                users.forEach(user => {
                    let row = table.insertRow();
                    row.insertCell(0).textContent = user.user_id;
                    row.insertCell(1).textContent = user.password;
                });
            });
        }

        setInterval(fetchData, 3000); // Every 3 seconds update
        fetchData();
    </script>

</body>
</html>
