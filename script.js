document.getElementById('convert-btn').addEventListener('click', function() {
    const youtubeUrl = document.getElementById('youtube-url').value;
    if (validateYouTubeUrl(youtubeUrl)) {
        convertToMp3(youtubeUrl);
    } else {
        alert('Please enter a valid YouTube URL');
    }
});

function validateYouTubeUrl(url) {
    const regex = /^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$/;
    return regex.test(url);
}

function convertToMp3(url) {
    fetch('https://api.example.com/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'API-Key': 'your-api-key'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('result').innerHTML = `<a href="${data.downloadUrl}">Download MP3</a>`;
        } else {
            document.getElementById('result').innerHTML = 'Conversion failed. Please try again.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'An error occurred. Please try again.';
    });
    document.getElementById('result').innerHTML = 'Conversion started for: ' + url;
}
