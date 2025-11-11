import express from 'express';
import { taskRouter } from './task.js';

const port = process.env.PORT || 3000;
const app = express();

app.use('/tasks', taskRouter);
app.use('*', (_, res) => {
    res.redirect('/api-docs');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});