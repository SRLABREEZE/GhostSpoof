import React, { useEffect, useState } from 'react';
import API from '../api';

function Dashboard() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          alert('Not authenticated');
          return;
        }
        const response = await API.get('/users/me', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUserData(response.data);
      } catch (error) {
        console.error(error);
        alert('Failed to load data');
      }
    };
    fetchUserData();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      {userData ? <p>Welcome, {userData.email}!</p> : <p>Loading...</p>}
    </div>
  );
}

export default Dashboard;
