// Referencias a elementos del DOM
const form = document.getElementById('addProjectForm');
const projectList = document.getElementById('projects');


form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const title = document.getElementById('project-title').value;
  const description = document.getElementById('project-description').value;
  const category = document.getElementById('project-category').value;
  
  if (title && description && category) {
    
    const projectItem = document.createElement('li');
    projectItem.innerHTML = `
      <strong>${title}</strong> (${category})
      <p>${description}</p>
      <button class="delete-btn">Eliminar</button>
    `;
    
  
    projectItem.querySelector('.delete-btn').addEventListener('click', () => {
      projectItem.remove();
    });
    
 
    projectList.appendChild(projectItem);
    
    
    form.reset();
  } else {
    alert('Por favor, completa todos los campos.');
  }
});
