<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dussehra & Diwali WhatsApp Status Generator</title>
  <style>
    body { 
      font-family: 'Segoe UI', sans-serif; 
      margin: 0; padding: 0; 
      background: radial-gradient(circle at top, #fff5d7, #ffe5b4, #ffd580); 
      overflow-x: hidden;
    }
    .container { max-width: 900px; margin: auto; text-align: center; position: relative; z-index: 2; }
    .step { padding: 40px; display: none; }
    .active { display: block; }
    .logo-main, .goddess-img { width: 180px; margin: 30px; }
    .festive-title { 
      color: #a0522d; 
      font-size: 2.8rem; 
      font-family: 'Baloo', cursive; 
      text-shadow: 2px 2px #ffd700, 0px 0px 25px #ff9933; 
      animation: glow 2s infinite alternate;
    }
    .step-in-btn { 
      padding: 18px 55px; 
      font-size: 1.2rem; 
      background: linear-gradient(45deg,#ffb347,#ffcc33); 
      border: none; border-radius: 16px; 
      margin-top: 40px; 
      box-shadow: 0 6px 22px #dab600; 
      cursor: pointer; 
      transition: 0.3s;
    }
    .step-in-btn:hover { transform: scale(1.05); }

    .template-gallery { display: flex; justify-content: center; gap: 32px; margin: 40px 0; flex-wrap: wrap; }
    .template-card { border: 3px solid #ffd700; border-radius: 15px; padding: 14px; box-shadow: 0 0 12px #b5b5b5; cursor: pointer; transition: 0.3s; background: #fffef5; }
    .template-card:hover { transform: scale(1.05); }

    /* Editor with decorative glowing border */
    .status-editor { 
      position: relative; 
      width: 360px; 
      margin: 40px auto; 
      border: 10px solid transparent; 
      border-image: url('https://i.ibb.co/VQHymf8/golden-border.png') 30 round;
      box-shadow: 0 0 25px #ffcc33, 0 0 60px #ff9933; 
      animation: pulseGlow 3s infinite;
    }
    .status-bg { width: 100%; border-radius: 4px; }
    .overlay-logo { position: absolute; top: 15px; right: 15px; width: 70px; height: 70px; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 12px gold; }
    .overlay-text { position: absolute; bottom: 60px; left: 20px; font-size: 22px; color: #ffeb3b; font-weight: bold; font-family: 'Baloo'; max-width: 280px; word-wrap: break-word; text-shadow: 2px 2px 5px #000; }
    .overlay-owner { position: absolute; bottom: 30px; left: 20px; font-size: 16px; color: #ffffff; max-width: 280px; word-wrap: break-word; text-shadow: 1px 1px 3px #000; }

    .payment-section { text-align: center; margin: 60px; }
    .upi-link { background: #25d366; padding: 12px 40px; color: #fff; border-radius: 25px; text-decoration: none; font-size: 1.3em; margin-top: 20px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.2);}
    .upi-link:hover { background: #1ebd59; }
    .thankyou-section { text-align: center; padding: 30px; background: #fffaf2; }

    /* Floating diyas */
    .diya {
      position: absolute;
      bottom: -100px;
      width: 60px;
      animation: floatUp 12s linear infinite;
      z-index: 1;
    }
    .diya:nth-child(1) { left: 10%; animation-delay: 0s; }
    .diya:nth-child(2) { left: 30%; animation-delay: 4s; }
    .diya:nth-child(3) { left: 60%; animation-delay: 2s; }
    .diya:nth-child(4) { left: 80%; animation-delay: 6s; }

    @keyframes floatUp {
      from { transform: translateY(0) rotate(0); opacity: 1; }
      to { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
    }

    /* Firework sparkles */
    .sparkle {
      position: absolute;
      width: 6px; height: 6px;
      background: gold;
      border-radius: 50%;
      animation: twinkle 2s infinite;
      z-index: 1;
    }
    @keyframes twinkle {
      0%, 100% { transform: scale(0.5); opacity: 0.5; }
      50% { transform: scale(1.3); opacity: 1; }
    }

    /* Glow animations */
    @keyframes glow {
      from { text-shadow: 2px 2px #ffd700, 0px 0px 15px #ff9933; }
      to { text-shadow: 2px 2px #fff176, 0px 0px 25px #ff6f00; }
    }
    @keyframes pulseGlow {
      0% { box-shadow: 0 0 20px #ffd700, 0 0 50px #ff8c00; }
      50% { box-shadow: 0 0 35px #ffcc33, 0 0 80px #ff4500; }
      100% { box-shadow: 0 0 20px #ffd700, 0 0 50px #ff8c00; }
    }
  </style>
  <link href="https://fonts.googleapis.com/css2?family=Baloo&display=swap" rel="stylesheet">
</head>
<body>
  <!-- Floating Diyas -->
  <img src="https://i.ibb.co/5rjRzVv/diya.png" class="diya" />
  <img src="https://i.ibb.co/5rjRzVv/diya.png" class="diya" />
  <img src="https://i.ibb.co/5rjRzVv/diya.png" class="diya" />
  <img src="https://i.ibb.co/5rjRzVv/diya.png" class="diya" />

  <!-- Random Sparkles -->
  <div class="sparkle" style="top:10%; left:20%; animation-delay:0s;"></div>
  <div class="sparkle" style="top:30%; left:70%; animation-delay:1s;"></div>
  <div class="sparkle" style="top:50%; left:40%; animation-delay:2s;"></div>
  <div class="sparkle" style="top:80%; left:60%; animation-delay:3s;"></div>

  <div class="container">
    <!-- Step 1 -->
    <div id="step1" class="step active">
      <img class="logo-main" src="assets/Logo.jpg" alt="Logo" />
      <img class="goddess-img" src="assets/fireworks.jpeg" alt="crackers" />
      <h1 class="festive-title">Welcome to the Grand Dussehra & Diwali Wishes Studio</h1>
      <button onclick="nextStep(2)" class="step-in-btn">Step In</button>
    </div>

    <!-- Step 2 -->
    <div id="step2" class="step">
      <h2>Enter Your Shop Details</h2>
      <form id="detailsForm">
        <input type="text" id="shopName" placeholder="Shop Name" required style="margin: 10px; padding: 10px; width: 250px;" />
        <input type="text" id="ownerName" placeholder="Owner Name" required style="margin: 10px; padding: 10px; width: 250px;" /><br><br>
        <input type="text" id="phone" placeholder="Phone" required style="margin: 10px; padding: 10px; width: 250px;" />
        <input type="file" id="logo" accept="image/*" required style="margin: 10px;" /><br><br>
        <button type="button" onclick="saveDetails()">Continue</button>
      </form>
    </div>

    <!-- Step 3 -->
    <div id="step3" class="step">
      <h2>Select a Template</h2>
      <div class="template-gallery">
        <div class="template-card" onclick="selectTemplate('assets/pexels-souvik-laha-3637528-10852670.jpg')">
          <img src="assets/pexels-souvik-laha-3637528-10852670.jpg" width="180" alt="Dussehra Wishes" />
          <div>Dussehra Divine Wishes</div>
        </div>
        <div class="template-card" onclick="selectTemplate('assets/Durga Maa.jpg')">
          <img src="assets/Durga Maa.jpg" width="180" alt="Victory of Good" />
          <div>Victory of Good</div>
        </div>
      </div>
    </div>

    <!-- Step 4 -->
    <div id="step4" class="step">
      <h2>Customize Your Status</h2>
      <div id="statusCard" class="status-editor">
        <img id="statusBg" class="status-bg" src="" alt="Status" />
        <img id="overlayLogo" class="overlay-logo" src="" alt="Logo" />
        <div id="overlayText" class="overlay-text"></div>
        <div id="overlayOwner" class="overlay-owner"></div>
      </div>
      <button onclick="downloadStatus()">Download & Continue</button>
    </div>

    <!-- Step 5 -->
    <div id="step5" class="step">
      <h2>Pay ₹49 to Unlock</h2>
      <img src="assets/upi-qr.png" width="200" alt="UPI QR" />
      <br><br>
      <a href="upi://pay?pa=bojjasrikumar0806-1@oksbi&pn=Srikumar+Bojja&am=49&cu=INR" class="upi-link" target="_blank" rel="noopener noreferrer">Pay Now with UPI</a>
      <button onclick="nextStep(6)">I've Paid</button>
    </div>

    <!-- Step 6 -->
    <div id="step6" class="step">
      <div class="thankyou-section">
        <img src="assets/Harathi.jpg" width="250" alt="Harathi" />
        <h2>Thank You & Happy Dussehra!</h2>
        <p>May Goddess Durga & Lord Sri Ram bless you with happiness and prosperity.</p>
        <audio controls autoplay>
          <source src="assets/devotional-song.mp3" type="audio/mpeg" />
          Your browser does not support the audio element.
        </audio>
      </div>
    </div>
  </div>

  <!-- Add html2canvas for download -->
  <script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
  <script>
    let currentStep = 1;
    let selectedTemplate = '';
    let ownerDetails = {};

    function nextStep(step) {
      document.getElementById('step' + currentStep).classList.remove('active');
      currentStep = step;
      document.getElementById('step' + currentStep).classList.add('active');
    }

    function saveDetails() {
      ownerDetails.shopName = document.getElementById('shopName').value;
      ownerDetails.ownerName = document.getElementById('ownerName').value;
      ownerDetails.phone = document.getElementById('phone').value;
      const logoFile = document.getElementById('logo').files[0];
      if (logoFile) {
        const reader = new FileReader();
        reader.onload = function(e) {
          ownerDetails.logoSrc = e.target.result;
          nextStep(3);
        };
        reader.readAsDataURL(logoFile);
      }
    }

    function selectTemplate(imgSrc) {
      selectedTemplate = imgSrc;
      document.getElementById('statusBg').src = imgSrc;
      document.getElementById('overlayText').textContent = ownerDetails.shopName;
      document.getElementById('overlayOwner').textContent = 'By: ' + ownerDetails.ownerName;
      if (ownerDetails.logoSrc) {
        document.getElementById('overlayLogo').src = ownerDetails.logoSrc;
      }
      nextStep(4);
    }

    async function downloadStatus() {
      const statusCard = document.getElementById("statusCard");
      const canvas = await html2canvas(statusCard, { scale: 2 });
      const link = document.createElement("a");
      link.download = "festive_status.png";
      link.href = canvas.toDataURL("image/png");
      link.click();
      nextStep(5);
    }
  </script>
</body>
</html>
