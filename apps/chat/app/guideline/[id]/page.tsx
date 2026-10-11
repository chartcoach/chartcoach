import { GuidelinePage } from "../../../components/guideline-page";

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  return <GuidelinePage id={(await params).id} />;
}
