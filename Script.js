document.getElementById('new-card-button').addEventListener('click', getNewCard);

function getNewCard() {
    fetch('/api/new_card')
        .then(response => response.json())
        .then(data => {
            displayBingoCard(data);
        })
        .catch(error => console.error('Error fetching bingo card:', error));
}

function displayBingoCard(cardData) {
    const cardElement = document.getElementById('bingo-card');
    cardElement.innerHTML = `
        <div class="column-header">B</div>
        <div class="column-header">I</div>
        <div class="column-header">N</div>
        <div class="column-header">G</div>
        <div class="column-header">O</div>
    `;

    const columns = ['B', 'I', 'N', 'G', 'O'];
    for (const col of columns) {
        cardData[col].forEach(number => {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.textContent = number;
            if (number === 'Free') {
                cell.classList.add('free');
            }
            cardElement.appendChild(cell);
        });
    }
}
