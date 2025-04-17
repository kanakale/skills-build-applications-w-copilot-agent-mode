import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://vigilant-dollop-457r6r5q7gj27r67-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity._id}>{activity.activity_type} - {activity.duration}</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;
