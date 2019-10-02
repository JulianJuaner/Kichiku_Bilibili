#show all data with points.
select * from bilibili.video_pts;
#select one video with id.
select *from bilibili.kichu_video where av=27756410;
#find top 100 authors by pts.
select av, authorid, authorname, title, max(pts) as pt from bilibili.video_pts group by(authorid) order by pt desc;
select count(pts) as pt, authorid, authorname from bilibili.video_pts group by (authorid, authorname);

#select top 100 UPs with their most famous video.
select UP.authorid, UP.authorname, UP.pt, UP.num, NEWV.av, NEWV.title, NEWV.pts as max_pt from 
	(select R.authorid, R.authorname, R.pt, R.num from 
		(select sum(pts) as pt, count(av) as num, authorid, authorname from bilibili.video_pts group by authorid, authorname) 
	as R order by R.pt desc limit 100) AS UP, 
    (select authorid, max(pts) as pt from bilibili.video_pts group by(authorid)) AS max_pts,
    (select av, authorid, title, pts from bilibili.video_pts) AS NEWV
where (max_pts.authorid=UP.authorid and NEWV.pts=max_pts.pt and max_pts.authorid=NEWV.authorid) order by UP.pt desc;

select sum(T.num), sum(T.viewcount), sum(T.pt) from (select R.authorid, R.authorname, R.pt, R.num, R.viewcount from 
		(select sum(pts) as pt, count(av) as num, authorid, authorname, sum(viewcount) as viewcount from bilibili.video_pts group by authorid, authorname) 
	as R order by R.pt desc limit 10) AS T;
    
select sum(coin)/165380, sum(viewcount)/165380, sum(share)/165380, sum(favorite)/165380 from bilibili.video_pts;

#original or transport (incomplete)
select count(av) from bilibili.video_pts WHERE (description like '%原创%' or description like '%自制%'
or keywords like '%原创%' or keywords like '%自制%' or title like '%原创%' or title like '%自制%');
select count(av) from bilibili.video_pts WHERE (description like '%sm%' or description like '%搬运%'
or keywords like '%sm%' or keywords like '%搬运%' or title like '%sm%' or title like '%搬运%');
