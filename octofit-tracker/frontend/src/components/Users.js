import React, { useEffect, useState } from 'react';

// Add the Django REST API endpoint suffix for Users
const API_ENDPOINT = '/api/users/';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`https://verbose-pancake-r4q9j4jwqpp257q6-8000.app.github.dev${API_ENDPOINT}`)
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Users</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.name}</td>
              <td>{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;