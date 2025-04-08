import React, { useEffect, useState } from 'react';

// Add the Django REST API endpoint suffix for Workouts
const API_ENDPOINT = '/api/workouts/';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(`https://verbose-pancake-r4q9j4jwqpp257q6-8000.app.github.dev${API_ENDPOINT}`)
      .then(response => response.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Workouts</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map(workout => (
            <tr key={workout.id}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;