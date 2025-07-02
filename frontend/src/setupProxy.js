const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');
const fs = require('fs');

module.exports = function(app) {
  // Servir demo.html directamente
  app.get('/demo.html', (req, res) => {
    const demoPath = path.join(__dirname, '../public/demo.html');
    if (fs.existsSync(demoPath)) {
      res.sendFile(demoPath);
    } else {
      res.status(404).send('demo.html not found');
    }
  });
  
  // Servir demo sin extensión también
  app.get('/demo', (req, res) => {
    const demoPath = path.join(__dirname, '../public/demo.html');
    if (fs.existsSync(demoPath)) {
      res.sendFile(demoPath);
    } else {
      res.status(404).send('demo.html not found');
    }
  });
};