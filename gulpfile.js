var gulp = require('gulp');

var sass = require('gulp-sass');

var browserSync = require('browser-sync');

gulp.task('sass',function(){
	gulp.src('static/myapp/scss/*.scss')
	.pipe(sass())
	.pipe(gulp.dest('static/myapp/dist/css'))
	.pipe(browserSync.reload({
		stream: true
	}))
});

gulp.task('watch',['browserSync','sass'],function(){
	gulp.watch('static/myapp/scss/*.scss',['sass']);
	gulp.watch('templates/**/*.html', browserSync.reload)
});

gulp.task('browserSync',function(){
	browserSync({
		//proxy to Django server
		proxy: "localhost:8000"
	})
});