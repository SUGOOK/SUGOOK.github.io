// API에서 데이터를 가져오는 JavaScript 코드
async function fetchData() {
    const conductance = 760;
    const pump = "IXH3050H";

    const response = await fetch(`https://sugook-github-io.onrender.com/api/multiply?conductance=${conductance}&pump=${pump}`);
    const data = await response.json();

    console.log(data); // {"result": 200, "pump": "IXH3050H"}

    // HTML에 결과 표시
    document.getElementById('output').innerText = `Result: ${data.result}, Pump: ${data.pump}`;
}

// 페이지 로드 시 API 호출
window.onload = fetchData;
