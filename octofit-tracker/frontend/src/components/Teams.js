import React, { useEffect, useState } from 'react';

// Add the Django REST API endpoint suffix for Teams
const API_ENDPOINT = '/api/teams/';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(`https://verbose-pancake-r4q9j4jwqpp257q6-8000.app.github.dev${API_ENDPOINT}`)
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Teams</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.id}>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;