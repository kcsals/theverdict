import Link from 'next/link';
import imgPerformance from '/public/performance.jpg';
import Hero from '@/components/hero';

export default function Performance() {
  return (
    <Hero
      imgData={imgPerformance}
      imgAlt='car factory'
      title='Performance Page'
    />
  );
}
