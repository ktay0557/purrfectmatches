import { useEffect, useRef, useState } from 'react';

// Allows automatic closing of nav when users clicks
const UseClickOutsideToggle = () => {
    const [expanded, setExpanded] = useState(false);
    const ref = useRef(null);

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (ref.current && !ref.current.contains(event.target)) {
                setExpanded(false);
            }
        };

        document.addEventListener("mouseup", handleClickOutside);
        return () => {
            document.removeEventListener("mouseup", handleClickOutside);
        };
    }, [ref]);

    return { expanded, setExpanded, ref };
};

export default UseClickOutsideToggle;