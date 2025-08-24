
  async function loadCSV() {
    const response = await fetch('data.csv');
    const csvText = await response.text();
    const rows = csvText.trim().split('\n').map(row => row.split(','));
    
    const table = document.getElementById('csv-table');
    table.innerHTML = ''; // Clear previous content

    rows.forEach((row, index) => {
      const tr = document.createElement('tr');
      row.forEach(cell => {
        const td = document.createElement(index === 0 ? 'th' : 'td');
        td.textContent = cell;
        tr.appendChild(td);
      });
      table.appendChild(tr);
    });
  }

  document.addEventListener('DOMContentLoaded', loadCSV);

