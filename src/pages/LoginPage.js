import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import backgroundImage from "../assets/What-Is-Applied-Psychology-Hero-Image.jpg";

function LoginPage() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    const registeredEmail = localStorage.getItem("registeredEmail");
    const registeredPassword = localStorage.getItem("registeredPassword");

    if (email === registeredEmail && password === registeredPassword) {
      navigate("/home");
    } else {
      setError("Böyle bir hesap bulunamadı. Lütfen kayıt olun.");
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      backgroundImage: `url(${backgroundImage})`,
      backgroundSize: "cover",
      backgroundPosition: "center",
      fontFamily: "Arial, sans-serif"
    }}>
      <div style={{
        background: "rgba(255, 255, 255, 0.9)",
        padding: "40px",
        borderRadius: "10px",
        boxShadow: "0 10px 25px rgba(0, 0, 0, 0.2)",
        width: "300px",
        textAlign: "center"
      }}>
        <h2 style={{ marginBottom: "20px", color: "#333" }}>MindHelp'e Hoşgeldiniz!</h2>
        <form onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="Email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              marginBottom: "15px",
              borderRadius: "5px",
              border: "1px solid #ccc",
              outline: "none"
            }}
          />
          <input
            type="password"
            placeholder="Şifre"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              marginBottom: "20px",
              borderRadius: "5px",
              border: "1px solid #ccc",
              outline: "none"
            }}
          />
          <button type="submit" style={{
            width: "100%",
            padding: "10px",
            borderRadius: "5px",
            border: "none",
            backgroundColor: "#667eea",
            color: "white",
            fontWeight: "bold",
            cursor: "pointer"
          }}>
            Giriş Yap
          </button>
        </form>
        {error && <p style={{ color: "red", marginTop: "15px" }}>{error}</p>}
        <p style={{ marginTop: "20px", fontSize: "14px" }}>
          Hesabınız yok mu?{" "}
          <a href="/register" style={{ color: "#667eea", textDecoration: "none", fontWeight: "bold" }}>
            Kayıt Ol
          </a>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
