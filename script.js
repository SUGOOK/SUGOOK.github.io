document.getElementById('input-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const a = parseFloat(document.getElementById('input-a').value);
    const b = parseFloat(document.getElementById('input-b').value);
    const c = parseFloat(document.getElementById('input-c').value);
    const d = parseFloat(document.getElementById('input-d').value);

    try {
        const response = await fetch('https://your-backend.onrender.com/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ a, b, c, d }),
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        document.getElementById('result').innerText = `Result: ${data.result}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error fetching result';
    }
});
