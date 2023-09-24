//const resources = [
//    { id: 1, name: 'Ресурс 1', type: 'Тип 1', current_speed: 50, max_speed: 100 },
//    { id: 2, name: 'Ресурс 2', type: 'Тип 2', current_speed: 75, max_speed: 120 },
//];
//
//const resourceTypes = [
//    { id: 1, name: 'Тип 1', max_speed: 100 },
//    { id: 2, name: 'Тип 2', max_speed: 120 },
//];
//
//function updateResourceList() {
//    const resourceList = document.getElementById('resourceList');
//    resourceList.innerHTML = '';
//
//    resources.forEach(resource => {
//        const li = document.createElement('li');
//        li.textContent = `ID: ${resource.id}, Имя: ${resource.name}, Тип: ${resource.type}, Скорость: ${resource.current_speed}`;
//        resourceList.appendChild(li);
//    });
//}
//
//function updateResourceTypeList() {
//    const resourceTypeList = document.getElementById('resourceTypeList');
//    resourceTypeList.innerHTML = '';
//
//    resourceTypes.forEach(resourceType => {
//        const li = document.createElement('li');
//        li.textContent = `ID: ${resourceType.id}, Имя: ${resourceType.name}, Макс. Скорость: ${resourceType.max_speed}`;
//        resourceTypeList.appendChild(li);
//    });
//}
//
//document.getElementById('refreshResources').addEventListener('click', updateResourceList);
//
//document.getElementById('refreshResourceTypes').addEventListener('click', updateResourceTypeList);
//
//updateResourceList();
//updateResourceTypeList();
