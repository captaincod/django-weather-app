document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('cityInput');
    const suggestionsBox = document.getElementById('suggestions');
    suggestionsBox.classList.add('hidden');

    input.addEventListener('input', async () => {
        const query = input.value.trim();
        if (query.length < 2) {
            suggestionsBox.innerHTML = '';
            suggestionsBox.classList.add('hidden');
            return;
        }

        const response = await fetch(`/autocomplete/?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        suggestionsBox.innerHTML = '';
        data.results.forEach(city => {
            const div = document.createElement('div');
            div.textContent = city;
            div.addEventListener('click', () => {
                input.value = city;
                suggestionsBox.innerHTML = '';
            });
            suggestionsBox.appendChild(div);
        });
        suggestionsBox.classList.remove('hidden');
    });

    document.addEventListener('click', (e) => {
        if (!suggestionsBox.contains(e.target) && e.target !== input) {
            suggestionsBox.innerHTML = '';
            suggestionsBox.classList.add('hidden');
        }
    });

    if (suggestionsBox.options.length <= 1) {
        suggestionsBox.classList.add('hidden');
    } else {
        suggestionsBox.classList.remove('hidden');
    }
});