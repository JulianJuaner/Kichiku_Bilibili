#show all data with points.
select * from bilibili.video_pts;
#select one video with id.
select *from bilibili.kichu_video where av=27756410;
#find top 100 authors by pts.
select av, authorid, authorname, title, max(pts) as pt from bilibili.video_pts group by(authorid) order by pt desc;
select count(pts) as pt, authorid, authorname from bilibili.video_pts group by (authorid, authorname);

select UP.authorid, UP.authorname, UP.pt, UP.num, NEWV.av, NEWV.title, NEWV.pts as max_pt from 
	(select R.authorid, R.authorname, R.pt, R.num from 
		(select sum(pts) as pt, count(av) as num, authorid, authorname from bilibili.video_pts group by authorid, authorname) 
	as R order by R.pt desc limit 100)AS UP, 
    (select authorid, max(pts) as pt from bilibili.video_pts group by(authorid)) AS max_pts,
    (select av, authorid, title, pts from bilibili.video_pts) AS NEWV
where (max_pts.authorid=UP.authorid and NEWV.pts=max_pts.pt and max_pts.authorid=NEWV.authorid) order by UP.pt desc;