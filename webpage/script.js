document.addEventListener('DOMContentLoaded', () => {
    const itemSelect = document.getElementById('itemSelect');
    const selectedItemsList = document.getElementById('selectedItemsList');
    const searchInput = document.getElementById('searchInput');

    // Function to filter the items in the drop-down list
    searchInput.addEventListener('input', () => {
        const filter = searchInput.value.toLowerCase();
        const options = itemSelect.getElementsByTagName('option');

        for (let i = 1; i < options.length; i++) { // Start at 1 to skip the default option
            const text = options[i].textContent.toLowerCase();
            if (text.includes(filter)) {
                options[i].style.display = '';
            } else {
                options[i].style.display = 'none';
            }
        }
    });

    itemSelect.addEventListener('change', () => {
        const selectedItem = itemSelect.value;

        if (selectedItem) {
            // Check if the item is already in the list
            const items = selectedItemsList.getElementsByTagName('li');
            let itemExists = false;
            for (let i = 0; i < items.length; i++) {
                if (items[i].textContent === selectedItem) {
                    itemExists = true;
                    break;
                }
            }

            // If the item does not exist, add it to the list
            if (!itemExists) {
                const li = document.createElement('li');
                li.textContent = selectedItem;

                // Add click event to remove item from selected list and add back to dropdown
                li.addEventListener('click', () => {
                    selectedItemsList.removeChild(li);
                    const option = document.createElement('option');
                    option.value = selectedItem;
                    option.textContent = selectedItem;
                    itemSelect.appendChild(option);
                });

                selectedItemsList.appendChild(li);

                // Remove the item from the dropdown
                const optionToRemove = itemSelect.querySelector(`option[value="${selectedItem}"]`);
                if (optionToRemove) {
                    itemSelect.removeChild(optionToRemove);
                }
            }

            // Reset the select element
            itemSelect.selectedIndex = 0;
        }
    });
});
