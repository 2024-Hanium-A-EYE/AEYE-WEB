import { useRouter } from 'next/navigation'; // next/router 대신 next/navigation 사용

const ResultPage = ({ searchParams }: { searchParams: { resultData?: string } }) => {
  const resultData = searchParams.resultData;

  if (!resultData) {
    return <p>Loading...</p>; // 데이터가 아직 로드되지 않았을 경우
  }

  const data = JSON.parse(resultData);

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold">이미지 업로드 결과</h1>
      <p>{data.message}</p>
      {data.imageUrl && (
        <img src={data.imageUrl} alt="업로드된 이미지" className="mt-4" />
      )}
    </div>
  );
};

export default ResultPage;
