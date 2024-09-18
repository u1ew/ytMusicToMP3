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
    // This is a placeholder function. You would need to integrate with a backend service or API
    // that handles the actual conversion.
    document.getElementById('result').innerHTML = 'Conversion started for: ' + url;
}
