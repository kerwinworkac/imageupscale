document.getElementById('upload-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);
  
  try {
    const response = await fetch('/upload', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error('Error occurred during upload');
    }

    const { upscaled_images } = await response.json();
    displayUpscaledImages(upscaled_images);
  } catch (error) {
    console.error('Error:', error);
  }
});

function displayUpscaledImages(upscaledImages) {
  const container = document.getElementById('preview-container');
  container.innerHTML = '';

  upscaledImages.forEach((image) => {
    const preview = document.createElement('div');
    preview.classList.add('image-preview');

    const img = document.createElement('img');
    img.src = `/images/${image}`;

    const button = document.createElement('button');
    button.textContent = 'Download';
    button.addEventListener('click', () =>{
      downloadImage(image);
    });

    preview.appendChild(img);
    preview.appendChild(button);
    container.appendChild(preview);
  });
}

function downloadImage(image) {
  const link = document.createElement('a');
  link.href = `/images/${image}`;
  link.download = image;
  link.click();
}