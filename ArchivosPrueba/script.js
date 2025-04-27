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
    
    const titleElement = document.createElement('strong');
    titleElement.textContent = title;
    projectItem.appendChild(titleElement);
    
    const categoryText = document.createTextNode(` (${category})`);
    projectItem.appendChild(categoryText);
    
    const descriptionElement = document.createElement('p');
    descriptionElement.textContent = description;
    projectItem.appendChild(descriptionElement);
    
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Eliminar';
    deleteButton.className = 'delete-btn';
    projectItem.appendChild(deleteButton);
    
    deleteButton.addEventListener('click', () => {
      projectItem.remove();
    });
    
 
    projectList.appendChild(projectItem);
    
    
    form.reset();
  } else {
    alert('Por favor, completa todos los campos.');
  }
});
