- To use a profile, in app startup, use: `-Dsping.profiles.active=dev`


## Best practices
1. Do not mix .yaml and .properties property files. Use one format.

## Controllers
2. `@RestController` vs `@Controller`. RestController is string specific.
3. `@ResponseBody` annotation sa return type may be removed if `@RestController` ang annotation sa class
4. For `manytomany`, add JsonIgnore
5. For one-to-many and many-to-one, add `@JsonbackReference` and `@JsonManagedReference`

## Error handling
1. See https://app.pluralsight.com/course-player?clipId=7b46ab45-74f3-4f78-a2bb-668ec5c91b67 @03:25

## Unit testing
1. See https://app.pluralsight.com/course-player?clipId=142ce3db-a0b9-4b8d-87fa-7072a47af3c9 @2:08

## JPA
- [Difference Between @JoinColumn and mappedBy](https://www.baeldung.com/jpa-joincolumn-vs-mappedby)

## S3
- [Upload to s3 bucket](https://medium.com/oril/uploading-files-to-aws-s3-bucket-using-spring-boot-483fcb6f8646)

## Other questions
- [Difference sa CRUDRepository and JPARepository](https://stackoverflow.com/questions/14014086/what-is-difference-between-crudrepository-and-jparepository-interfaces-in-spring)

## Youtube playlist
- https://www.youtube.com/watch?v=avvrsnYFXIE
