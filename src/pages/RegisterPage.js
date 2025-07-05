import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import backgroundImage from "../assets/What-Is-Applied-Psychology-Hero-Image.jpg";

function RegisterPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = (e) => {
    e.preventDefault();

    // Verileri localStorage'a kaydet
    localStorage.setItem("registeredUsername", username);
    localStorage.setItem("registeredEmail", email);
    localStorage.setItem("registeredPhone", phone);
    localStorage.setItem("registeredPassword", password);

    alert("Kayıt başarılı! Giriş yapabilirsiniz.");
    navigate("/");
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
        <h2 style={{ marginBottom: "20px", color: "#333" }}>Kayıt Ol</h2>
        <form onSubmit={handleRegister}>
          <input
            type="text"
            placeholder="Kullanıcı Adı"
            required
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            style={inputStyle}
          />
          <input
            type="email"
            placeholder="Email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={inputStyle}
          />
          <input
            type="tel"
            placeholder="Telefon Numarası"
            required
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            style={inputStyle}
          />
          <input
            type="password"
            placeholder="Şifre"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={inputStyle}
          />
          <button type="submit" style={buttonStyle}>
            Kayıt Ol
          </button>
        </form>
        <p style={{ marginTop: "20px", fontSize: "14px" }}>
          Zaten hesabınız var mı?{" "}
          <a href="/" style={{ color: "#667eea", textDecoration: "none", fontWeight: "bold" }}>
            Giriş Yap
          </a>
        </p>
      </div>
    </div>
  );
}

// Stil objeleri dışarı çıkarıldı
const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "15px",
  borderRadius: "5px",
  border: "1px solid #ccc",
  outline: "none"
};

const buttonStyle = {
  width: "100%",
  padding: "10px",
  borderRadius: "5px",
  border: "none",
  backgroundColor: "#667eea",
  color: "white",
  fontWeight: "bold",
  cursor: "pointer"
};

export default RegisterPage;
