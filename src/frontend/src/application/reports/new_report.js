"use strict";

document.addEventListener("DOMContentLoaded", () => {
  const calendarGrid = document.getElementById("calendar-grid");
  const currentMonthEl = document.getElementById("current-month");
  const taskModal = document.getElementById("task-modal");
  const taskInput = document.getElementById("task-input");
  const taskStatus = document.getElementById("task-status");
  const modalDate = document.getElementById("modal-date");
  const cancelModal = document.getElementById("cancel-modal");
  const saveTasks = document.getElementById("save-tasks");
  let currentDate = new Date();
  let tasks = {};

  // Demo tasks for placeholders (multiple tasks per day)
  const demoTasks = {
    1: [
      { description: "Team Meeting", status: "in-progress" },
      { description: "Submit Report", status: "completed" },
    ],
    5: [
      { description: "Submit Report", status: "completed" },
      { description: "Client Call", status: "overdue" },
      { description: "Code Review", status: "in-progress" },
    ],
    10: [
      { description: "Client Call", status: "overdue" },
      { description: "Project Deadline", status: "completed" },
    ],
    15: [
      { description: "Code Review", status: "in-progress" },
      { description: "Marketing Plan", status: "completed" },
      { description: "Bug Fixing", status: "overdue" },
      { description: "User Testing", status: "in-progress" },
    ],
    20: [
      { description: "Project Deadline", status: "completed" },
      { description: "Team Standup", status: "in-progress" },
    ],
    22: [
      { description: "Project Deadline", status: "completed" },
      { description: "Team Standup", status: "in-progress" },
    ],
    25: [
      { description: "Launch Event", status: "overdue" },
      { description: "Performance Review", status: "completed" },
      { description: "Sprint Planning", status: "in-progress" },
    ],
    30: [
      { description: "Launch Event", status: "overdue" },
      { description: "Performance Review", status: "completed" },
      { description: "Sprint Planning", status: "in-progress" },
    ],
  };

  const renderCalendar = (date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const lastDay = new Date(year, month + 1, 0).getDate();

    // Update month/year display
    currentMonthEl.textContent = date.toLocaleDateString("en-US", {
      month: "long",
      year: "numeric",
    });

    // Clear existing days
    calendarGrid.innerHTML = "";

    // Generate days
    for (let day = 1; day <= lastDay; day++) {
      const dayCell = document.createElement("div");
      dayCell.className =
        "p-2 border rounded-md bg-gray-100 relative group cursor-pointer hover:bg-gray-200 transition";
      dayCell.innerHTML = `
        <div class="flex justify-between">
          <span class="font-bold text-gray-700">${day}</span>
        </div>
        <ul id="tasks-${day}" class="mt-2 space-y-1 max-h-16 overflow-hidden"></ul>
      `;

      // Add click event to open the modal
      dayCell.addEventListener("click", () => openTaskModal(day));

      // Retrieve tasks for this day
      if (demoTasks[day] && demoTasks[day].length > 0) {
        const taskList = dayCell.querySelector(`#tasks-${day}`);

        demoTasks[day].forEach((task, index) => {
          if (index < 2) {
            // Show up to 2 tasks directly
            const taskEl = document.createElement("li");
            let bgColor;
            if (task.status === "in-progress") bgColor = "bg-blue-100 text-blue-800";
            else if (task.status === "completed") bgColor = "bg-green-100 text-green-800";
            else if (task.status === "overdue") bgColor = "bg-red-100 text-red-800";

            taskEl.className = `${bgColor} px-2 py-1 rounded-md text-xs font-medium truncate`;
            taskEl.textContent = task.description;
            taskList.appendChild(taskEl);
          }
        });

        // If there are more than 2 tasks, show a "+X more" button
        if (demoTasks[day].length > 2) {
          const moreTasks = document.createElement("button");
          moreTasks.className = "text-xs text-blue-500 mt-1 hover:underline";
          moreTasks.textContent = `+${demoTasks[day].length - 2} more`;
          moreTasks.addEventListener("click", (event) => showTaskTooltip(day, event));
          taskList.appendChild(moreTasks);
        }
      }

      calendarGrid.appendChild(dayCell);
    }
  };

  // Function to show all tasks in a tooltip
  const showTaskTooltip = (day, event) => {
    // Remove any existing tooltips
    document.querySelectorAll(".tooltip").forEach((el) => el.remove());

    const tooltip = document.createElement("div");
    tooltip.className =
      "absolute left-0 top-full mt-2 w-48 bg-white border shadow-lg rounded-lg p-2 text-xs text-gray-800 z-50 tooltip";
    tooltip.innerHTML = demoTasks[day]
      .map(
        (task) =>
          `<p class="py-1 px-2 rounded-md ${
            task.status === "in-progress"
              ? "bg-blue-100 text-blue-800"
              : task.status === "completed"
                ? "bg-green-100 text-green-800"
                : "bg-red-100 text-red-800"
          }">${task.description}</p>`,
      )
      .join("");

    // Append tooltip to the button
    event.target.parentElement.appendChild(tooltip);

    // Remove tooltip when clicking outside
    document.addEventListener(
      "click",
      () => {
        tooltip.remove();
      },
      { once: true },
    );
  };

  const openTaskModal = (day) => {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth() + 1; // Month is 0-indexed
    modalDate.textContent = `${month}/${day}/${year}`;
    taskInput.value =
      tasks[`${year}-${month}-${day}`]?.map((t) => t.description).join("\n") || "";
    taskModal.classList.remove("hidden");
  };

  const closeTaskModal = () => {
    taskModal.classList.add("hidden");
  };

  const saveTaskModal = () => {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth() + 1; // Month is 0-indexed
    const day = parseInt(modalDate.textContent.split("/")[1]);
    const taskText = taskInput.value.trim();
    const status = taskStatus.value;

    if (taskText) {
      tasks[`${year}-${month}-${day}`] = taskText.split("\n").map((desc) => ({
        description: desc,
        status,
      }));
    } else {
      delete tasks[`${year}-${month}-${day}`];
    }

    closeTaskModal();
    renderCalendar(currentDate);
  };

  // Event Listeners
  if (document.getElementById("prev-month")) {
    document.getElementById("prev-month").addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() - 1);
      renderCalendar(currentDate);
    });
  }
  if (document.getElementById("next-month")) {
    document.getElementById("next-month").addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() + 1);
      renderCalendar(currentDate);
    });
  }
  if (document.getElementById("today-btn")) {
    document.getElementById("today-btn").addEventListener("click", () => {
      currentDate = new Date();
      renderCalendar(currentDate);
    });
  }
  if (cancelModal) {
    cancelModal.addEventListener("click", closeTaskModal);
  }
  if (saveTasks) {
    saveTasks.addEventListener("click", saveTaskModal);
  }

  if (calendarGrid) {
    // Initial render
    renderCalendar(currentDate);
  }
});
