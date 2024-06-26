import './App.css';
import NavBar from './components/NavBar';
import { Routes, Route, useNavigate } from "react-router-dom";
import WelcomePage from './pages/WelcomePage';
import LearnPage from './pages/LearnPage';
import ProfilePage from './pages/ProfilePage';
import LeaderBoardPage from './pages/LeaderboardPage';
import LoginPage from './pages/LoginPage';
import Courses  from './pages/CoursesPage';
import { useState } from 'react';

function App() {
  
  const [loggedIn,setLoggedIn] = useState(
    localStorage.getItem("access_token")!==null 
  );
  const navigate = useNavigate();
  console.log("AM I LOGGED IN:",loggedIn);

  
  const loginHandle =(access_token, id)=>{
    localStorage.setItem('access_token', access_token)
    localStorage.setItem('user_id', id)
    setLoggedIn(true);
    navigate("/")
  }

  const handleLogout = () => {
    localStorage.clear();
    setLoggedIn(false)
    navigate("/")
};

  


  return (
    <div>
      <div className="bg-gradient-to-t from-red-700 ...">
        <NavBar loggedIn={loggedIn} />
      </div>
      <div>
        <Routes>
          <Route path="/" element={<WelcomePage />}/>
          <Route path="/learn" element={<LearnPage />}/>
          <Route path="/profile" element={<ProfilePage callback={handleLogout} />}/>
          <Route path="/leaderboard" element={<LeaderBoardPage />}/>
          <Route path="/courses" element={<Courses />}/>
          <Route path="/login" element={<LoginPage callback={loginHandle}/>}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
