// Function to extract module names and sub-modules from all sections
function extractModulesAndSubModules() {
    const sections = document.querySelectorAll('section.group__topic-wrapper');
    const result = [];

    sections.forEach(section => {
        // Extract module name
        const moduleNameElement = section.querySelector('.topic__title');
        const moduleName = moduleNameElement ? moduleNameElement.textContent.trim() : 'Unknown Module';

        // Extract sub-modules
        const subModules = [];
        const subModuleWrapperElements = section.querySelectorAll('.level__title-wrapper');
        
        subModuleWrapperElements.forEach(wrapper => {
            const pElement = wrapper.querySelector('.level__title > span');
            if (pElement) {
                const subModuleText = pElement.textContent.trim();
                subModules.push(subModuleText);
            }
        });

        // Store the module name and its sub-modules
        result.push({
            moduleName: moduleName,
            subModules: subModules
        });
    });

    return result;
}

// Function to download JSON data as a file
function downloadJSON(data, filename) {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Call the function and download the result as JSON file
const modulesAndSubModules = extractModulesAndSubModules();
downloadJSON(modulesAndSubModules, 'modules_and_submodules.json');
