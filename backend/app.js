const express = require('express');
const contactRoutes = require('./routes/contact');
const cors = require('cors');

const app = express();

// 中间件
app.use(cors());
app.use(express.json());

// 路由
app.use('/api', contactRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`服务器运行在端口 ${PORT}`);
});
