## INSTALL

1. Download from https://maven.apache.org/download.cgi
2. Set environment variables:
    - MAVEN_HOME is for Maven 1, M2_HOME is for Maven 2 and later
    
## SETUP MULTI-MODULE PROJECT
1. `$ mvn archetype:generate`
2. Change packaging to `pom`
3. cd to parent folder and run `$ mvn archetype:generate` again. Maven will recognize the package=pom and will add as modules.
