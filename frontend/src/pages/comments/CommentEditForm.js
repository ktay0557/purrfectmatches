import React, { useState } from "react";
import { toast } from "react-toastify";

import Form from "react-bootstrap/Form";

import styles from "../../styles/CommentCreateEditForm.module.css";

import { axiosRes } from "../../api/axiosDefaults";

function CommentEditForm(props) {
    const { id, content, setShowEditForm, setComments } = props;

    const [formContent, setFormContent] = useState(content);

    // Handle form changes
    const handleChange = (event) => {
        setFormContent(event.target.value);
    };

    // Handle form submissions
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axiosRes.put(`/comments/${id}/`, {
                content: formContent.trim(),
            });
            setComments((prevComments) => ({
                ...prevComments,
                results: prevComments.results.map((comment) => {
                    return comment.id === id
                        ? {
                            ...comment,
                            content: formContent.trim(),
                            updated_at: "now",
                        }
                        : comment;
                }),
            }));
            toast.success("Comment edited successfully", {position: "top-center"});
            setShowEditForm(false);
        } catch (err) {
            toast.error("Comment not updated. Please try again", {position: "top-center"});
            // console.log(err);
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group className="pr-1">
                <Form.Control
                    className={styles.Form}
                    as="textarea"
                    value={formContent}
                    onChange={handleChange}
                    rows={2}
                />
            </Form.Group>
            <div className="text-right">
                <button
                    className={styles.Button}
                    onClick={() => setShowEditForm(false)}
                    type="button"
                >
                    cancel
                </button>
                <button
                    className={styles.Button}
                    disabled={!content.trim()}
                    type="submit"
                >
                    update
                </button>
            </div>
        </Form>
    );
}

export default CommentEditForm;