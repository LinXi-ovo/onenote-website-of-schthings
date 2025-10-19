const express = require('express');
const router = express.Router();
const nodemailer = require('nodemailer');

// 配置邮件发送器
const transporter = nodemailer.createTransport({
  service: 'qq',
  auth: {
    user: '3361759150@qq.com',
      pass: 'qwqelakwztyjcjfd' // 注意：这里需要使用QQ邮箱的授权码，不是QQ密码
  }
});

router.post('/contact', async (req, res) => {
  try {
    const { name, email, message, timestamp } = req.body;

    // 验证必填字段
    if (!name || !email || !message) {
      return res.status(400).json({ error: '请填写所有必填字段' });
    }

    // 构建邮件内容
    const mailOptions = {
      from: '3361759150@qq.com',
      to: 'ningmuzee8080@2925.com',
      subject: `来自网站的留言 - ${name}`,
      html: `
        <h3>新的留言</h3>
        <p><strong>姓名：</strong> ${name}</p>
        <p><strong>邮箱：</strong> ${email}</p>
        <p><strong>留言时间：</strong> ${timestamp}</p>
        <p><strong>留言内容：</strong></p>
        <p>${message}</p>
      `
    };

    // 发送邮件
    await transporter.sendMail(mailOptions);

    res.status(200).json({ message: '留言已成功发送' });
  } catch (error) {
    console.error('发送邮件失败:', error);
    res.status(500).json({ error: '发送失败，请稍后重试' });
  }
});

module.exports = router;
