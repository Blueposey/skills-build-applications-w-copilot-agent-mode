import React, { useEffect, useState } from 'react';

// Add the Django REST API endpoint suffix for Activities
const API_ENDPOINT = '/api/activities/';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(`https://verbose-pancake-r4q9j4jwqpp257q6-8000.app.github.dev${API_ENDPOINT}`)
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h1 className="text-center my-4">Activities</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Type</th>
            <th>Duration (minutes)</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;