document.addEventListener("DOMContentLoaded", function () {
    const menu = document.getElementById("contextMenu");
    let selectedLessonId = null;

    document.addEventListener("contextmenu", function (e) {
        const lessonBox = e.target.closest(".lesson");

        if (lessonBox) {
            e.preventDefault();
            selectedLessonId = lessonBox.dataset.lessonId;  // ← store ID

            menu.style.left = `${e.pageX}px`;
            menu.style.top = `${e.pageY}px`;
            menu.style.display = "block";
        } else {
            menu.style.display = "none";
        }
    });

    document.addEventListener("click", function () {
        menu.style.display = "none";
    });


    function goToAction(action) {
        if (selectedLessonId) {
            window.location.href = `/${action}/${selectedLessonId}`;
        }
    }


    document.getElementById("editOption").addEventListener("click", function () {
        goToAction("edit");
    });

    document.getElementById("duplicateOption").addEventListener("click", function () {
        if (selectedLessonId) {
            window.location.href = `/duplicate/${selectedLessonId}`;
        }
    });

    document.getElementById("detailOption").addEventListener("click", function () {
        if (selectedLessonId) {
            window.location.href = `/detail/${selectedLessonId}`;
        }
    });

    document.getElementById("togglePaidOption").addEventListener("click", function () {
        if (selectedLessonId) {
            fetch(`/toggle_paid/${selectedLessonId}`, { method: 'POST' })
                .then(response => {
                    if (response.ok) {
                        alert("Paid status updated!");
                        location.reload(); // Refresh to see the updated value
                    } else {
                        alert("Something went wrong while updating.");
                    }
                })
                .catch(() => {
                    alert("Request failed.");
                });
        }
    });

    document.getElementById("toggleDeleteOption").addEventListener("click", function () {
        if (confirm("Are you sure you want to delete this class?")) {
            fetch(`/toggle_delete/${selectedLessonId}`, { method: 'POST' })
                .then(response => {
                    if (response.ok) {
                        alert("Class successfully deleted!");
                        location.reload(); // Refresh to see the updated value
                    } else {
                        alert("Something went wrong while updating.");
                    }
                })
                .catch(() => {
                    alert("Request failed.");
                });
        }
    });

});

let selectedLessons = new Set();

// Handle lesson box click to toggle selection
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.lesson').forEach(function (box) {
        box.addEventListener('click', function () {
            const lessonId = this.dataset.lessonId;

            if (selectedLessons.has(lessonId)) {
                selectedLessons.delete(lessonId);
                this.classList.remove('selected-lesson');
            } else {
                selectedLessons.add(lessonId);
                this.classList.add('selected-lesson');
            }

            console.log('Current selected lessons:', Array.from(selectedLessons));
        });
    });

    // Attach listener to the process button
    const processButton = document.getElementById('processSelectedBtn');
    if (processButton) {
        processButton.addEventListener('click', function () {
            submitSelectedLessons();
        });
    }
});

// Submit function to send selected IDs to backend
function submitSelectedLessons() {
    const form = document.getElementById('selectionForm');
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'selected_lessons';
    input.value = Array.from(selectedLessons).join(',');
    form.appendChild(input);
    form.submit();
}

function showExtraFields() {
    const option = document.getElementById('option').value;
    const copyField = document.getElementById('copyDateField');

    // Hide by default
    copyField.style.display = 'none';

    if (option === 'Copy') {
        copyField.style.display = 'block';
    }
}